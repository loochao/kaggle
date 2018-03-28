import functions
from sklearn.decomposition import PCA
from sklearn import svm


def get_result():
    train_data, train_label, test_data = functions.read_data_from_csv()

    rate = 0.5
    new_train_data = functions.shrink_img(train_data, rate=rate)
    new_test_data = functions.shrink_img(test_data, rate=rate)

    print('new_train_data.shape={}'.format(new_train_data.shape))

    pca_model = PCA(n_components=35, whiten=True)
    pca_model.fit(new_train_data)
    new_train_data = pca_model.transform(new_train_data)
    new_test_data = pca_model.transform(new_test_data)

    svm_model = svm.SVC(C=4)
    svm_model.fit(new_train_data, train_label)
    test_label = svm_model.predict(new_test_data)
    return test_label


if __name__ == '__main__':
    result = get_result()
    functions.save_result(result)
